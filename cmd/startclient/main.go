package main

import (
	"log"
	"time"

	pb "github.com/juandes/teamaqua/api/v1"

	"github.com/golang/protobuf/ptypes"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

const (
	address          = "localhost:50051"
	defaultName      = "world"
	shouldCreateUser = true
)

func main() {
	startClient()
}

func startClient() {
	log.Println("Starting client...")
	// Start the client
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}

	c := pb.NewDrinkWaterClient(conn)

	tsProto, err := ptypes.TimestampProto(time.Now())
	if err != nil {
		log.Fatalf("Error creating proto time: %v", err)
	}

	_, err = c.LogSplash(context.Background(), &pb.Splash{
		Amount: 1234,
		Ts:     tsProto,
	})

	if err != nil {
		log.Fatalf("Error in LogSplash: %v", err)
	}

}
