package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"

	"github.com/christopher-demarco/aoc-2024/internal/input"
)

func sortedCopy(list []int) []int {
	sorted := make([]int, len(list))
	copy(sorted, list)
	sort.Ints(sorted)
	return sorted
}

func parseIntField(field, columnName string) (int, error) {
	val, err := strconv.Atoi(field)
	if err != nil {
		return 0, fmt.Errorf("error parsing %s: %w", columnName, err)
	}
	return val, nil
}

func TotalDistance(left, right []int) (int, error) {
	if len(left) != len(right) {
		return 0, fmt.Errorf("length mismatch: %d vs %d", len(left), len(right))
	}

	var total int
	for i := range left {
		delta := left[i] - right[i]
		if delta < 0 {
			delta = -delta
		}
		total += delta
	}

	return total, nil
}

func Similarity(left, right []int) int {
	freq := make(map[int]int)
	for _, v := range right {
		freq[v]++
	}

	var total int
	for _, v := range left {
		total += v * freq[v]
	}

	return total
}

func LoadColumns(filename string) ([]int, []int, error) {
	lines, err := input.LoadLines(filename)
	if err != nil {
		return nil, nil, err
	}

	var col1, col2 []int

	for _, line := range lines {
		fields := strings.Fields(line)

		if len(fields) != 2 {
			continue
		}

		val1, err := parseIntField(fields[0], "first column")
		if err != nil {
			return nil, nil, err
		}

		val2, err := parseIntField(fields[1], "second column")
		if err != nil {
			return nil, nil, err
		}

		col1 = append(col1, val1)
		col2 = append(col2, val2)
	}

	return col1, col2, nil
}

func main() {
	col1, col2, err := LoadColumns("input.dat")
	if err != nil {
		panic(err)
	}

	col1 = sortedCopy(col1)
	col2 = sortedCopy(col2)
	total_distance, err := TotalDistance(col1, col2)
	if err != nil {
		panic(err)
	}
	fmt.Println(total_distance)

	similarity := Similarity(col1, col2)
	fmt.Println(similarity)
}
