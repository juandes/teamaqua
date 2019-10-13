package main

import (
	"context"
	"log"
	"net"

	"cloud.google.com/go/bigquery"
	firebase "firebase.google.com/go"
	pb "github.com/juandes/teamaqua/api/v1"
	"github.com/juandes/teamaqua/endpoint"
	"github.com/spf13/pflag"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

const (
	port = ":50051"
)

var (
	projectID *string = pflag.String("gcp-project", "", "GCP Project ID")
	bqDataset *string = pflag.String("bq-dataset", "", "")
	bqTable   *string = pflag.String("bq-table", "", "")
)

func init() {
	pflag.Parse()
}

func main() {
	log.Println("Starting server...")

	ctx := context.Background()

	client, err := bigquery.NewClient(ctx, *projectID)
	if err != nil {
		log.Fatalf("Error creating BQ client: %v", err)
	}

	myDataset := client.Dataset(*bqDataset)
	table := myDataset.Table(*bqTable)
	u := table.Uploader()

	// start the grpc server in a goroutine anon function
	go func() {
		lis, err := net.Listen("tcp", port)
		if err != nil {
			log.Fatalf("failed to listen: %v", err)
		}
		s := grpc.NewServer()
		pb.RegisterDrinkWaterServer(s, endpoint.NewService(u))

		// Register reflection service on gRPC server.
		reflection.Register(s)
		log.Print("Serving...")

		if err := s.Serve(lis); err != nil {
			log.Fatalf("failed to serve: %v", err)
		}
	}()

	//opt := option.WithCredentialsFile("path/to/serviceAccountKey.json")
	_, err = firebase.NewApp(ctx, nil)
	if err != nil {
		log.Printf("error initializing app: %v", err)
	}

	// TODO: dirty hack, fix it later
	select {}

}
