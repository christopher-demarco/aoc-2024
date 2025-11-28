package main

import "testing"

func TestTotalDistance(t *testing.T) {
	left := []int{3, 10, 7}
	right := []int{1, 16, 4}

	total, err := TotalDistance(left, right)
	if err != nil {
		t.Fatalf("TotalDistance returned error: %v", err)
	}

	const want = 11
	if total != want {
		t.Fatalf("TotalDistance = %d, want %d", total, want)
	}
}

func TestTotalDistanceLengthMismatch(t *testing.T) {
	_, err := TotalDistance([]int{1}, []int{1, 2})
	if err == nil {
		t.Fatalf("expected error for mismatched lengths")
	}
}

func TestSimilarity(t *testing.T) {
	left := []int{3, 4, 3, 2}
	right := []int{3, 1, 3, 2, 3}

	total := Similarity(left, right)
	const want = 20
	if total != want {
		t.Fatalf("Similarity = %d, want %d", total, want)
	}
}
