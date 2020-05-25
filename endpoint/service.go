package endpoint

import (
	"context"
	"log"

	"cloud.google.com/go/bigquery"
	"github.com/golang/protobuf/ptypes"
	pb "github.com/juandes/teamaqua/api/v1"
)

// Service implement the gRPC endpoints
type Service struct {
	splashes []*pb.Splash
	uploader *bigquery.Uploader
}

// NewService creates a new Service
func NewService(u *bigquery.Uploader) *Service {
	return &Service{
		splashes: []*pb.Splash{},
		uploader: u,
	}
}

// LogSplash writes a Splash event to BigQuery
func (s *Service) LogSplash(ctx context.Context, in *pb.Splash) (*pb.LogSplashResponse, error) {
	log.Println(in)

	s.splashes = append(s.splashes, in)
	err := s.uploader.Put(ctx, in)
	if err != nil {
		// TODO: Handle error better and don't just exit :/
		log.Fatalf("Error uploading to BQ: %v", err)
	}

	return &pb.LogSplashResponse{
		Ok: true,
	}, nil
}

// WaterConsumed checks the amount of water consumed since time in.
func (s *Service) WaterConsumed(ctx context.Context, in *pb.Since) (*pb.WaterConsumedSince, error) {
	var waterConsumed int32
	since, err := ptypes.Timestamp(in.Ts)
	if err != nil {
		log.Fatalf("Error converting ptypes.Timestamp to time: %v", err)
	}

	for _, splash := range s.splashes {
		splashTime, err := ptypes.Timestamp(splash.Ts)
		if err != nil {
			log.Fatalf("Error converting ptypes.Timestamp to time: %v", err)
		}

		if splashTime.After(since) {
			waterConsumed += splash.Amount
		}
	}

	return &pb.WaterConsumedSince{
		Amount: waterConsumed,
	}, nil
}
