package input

import (
	"os"
	"path/filepath"
	"testing"
)

func TestLoadLinesReturnsFileContents(t *testing.T) {
	dir := t.TempDir()
	filename := filepath.Join(dir, "example.txt")

	if err := os.WriteFile(filename, []byte("one\ntwo\n"), 0o600); err != nil {
		t.Fatalf("failed to write temp file: %v", err)
	}

	lines, err := LoadLines(filename)
	if err != nil {
		t.Fatalf("LoadLines returned error: %v", err)
	}

	want := []string{"one", "two"}
	if len(lines) != len(want) {
		t.Fatalf("unexpected number of lines: got %d, want %d", len(lines), len(want))
	}

	for i := range want {
		if lines[i] != want[i] {
			t.Fatalf("line %d mismatch: got %q, want %q", i, lines[i], want[i])
		}
	}
}

func TestLoadLinesMissingFile(t *testing.T) {
	_, err := LoadLines("does-not-exist")
	if err == nil {
		t.Fatalf("expected error when file is missing")
	}
}
