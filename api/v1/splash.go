package api

import "cloud.google.com/go/bigquery"

// Save implements the ValueSaver interface.
func (s *Splash) Save() (map[string]bigquery.Value, string, error) {
	return map[string]bigquery.Value{
		"ts":     s.Ts.Seconds,
		"amount": s.Amount,
	}, "", nil
}
