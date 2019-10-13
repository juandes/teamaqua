package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"firebase.google.com/go/messaging"

	firebase "firebase.google.com/go"
	"github.com/golang/protobuf/ptypes"
	pb "github.com/juandes/teamaqua/api/v1"
	"github.com/spf13/pflag"
	"google.golang.org/api/option"
	"google.golang.org/grpc"
)

const (
	address         = "localhost:50051"
	minutesInterval = 30
)

var (
	token             *string = pflag.String("token", "", "Firebase Token")
	projectID         *string = pflag.String("project-id", "", "Firebase Project ID")
	googleCredentials *string = pflag.String("google-credentials", "", "Google Service Account")
)

func init() {
	pflag.Parse()
}

func main() {
	log.Println("Starting Reminder service...")
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}

	ctx := context.Background()
	c := pb.NewDrinkWaterClient(conn)
	opt := option.WithCredentialsFile(*googleCredentials)

	fb, err := firebase.NewApp(ctx, &firebase.Config{
		ProjectID: *projectID,
	}, opt)

	if err != nil {
		log.Panicf("error initializing app: %v", err)
	}

	fbMessaging, err := fb.Messaging(ctx)
	if err != nil {
		log.Panicf("error initializing Firebase Messaging client app: %v", err)
	}

	response, err := fbMessaging.Send(ctx, &messaging.Message{
		Token: *token,
		Notification: &messaging.Notification{
			Title: "Hello!",
			Body:  "Reminder service running ...",
		},
		Data: map[string]string{},
	})

	if err != nil {
		log.Printf("Error sending Firebase notification: %v", err)
	}
	log.Println(response)

	go func() {
		interval := time.NewTicker(minutesInterval * time.Minute)

		for {
			select {
			case <-interval.C:
				var title string
				var body string

				log.Println("Executing...")
				// current time minus minutes interval
				t := time.Now().Add(time.Duration(-minutesInterval) * time.Minute)

				timestampProto, err := ptypes.TimestampProto(t)
				if err != nil {
					log.Fatalf("Error converting time to proto Timestamp: %v", err)
					continue
				}

				waterConsumed, err := c.WaterConsumed(ctx, &pb.Since{
					Ts: timestampProto,
				})
				if err != nil {
					log.Printf("Error calling WaterConsumed: %v", err)
					continue
				}

				if waterConsumed.Amount == 0 {
					title = "Reminder!"
					body = fmt.Sprintf("You havent drink anything in the last %d minutes", minutesInterval)
				} else {
					title = "Good job!"
					body = fmt.Sprintf("You had drunk %d in the last %d minutes", waterConsumed.Amount, minutesInterval)
				}

				response, err := fbMessaging.Send(ctx, &messaging.Message{
					Token: *token,
					Notification: &messaging.Notification{
						Title: title,
						Body:  body,
					},
					Data: map[string]string{},
				})

				if err != nil {
					log.Printf("Error sending Firebase notification: %v", err)
				}
				log.Println(response)

			}

		}

	}()

	http.HandleFunc("/", handler)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi!")
}
