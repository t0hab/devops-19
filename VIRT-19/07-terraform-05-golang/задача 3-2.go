package main

import "fmt"

func main() {
	x := []int{55, 96, 86, 68, 57, 82, 63, 70, 37, 34, 83, 27, 19, 97, 9, 17}
	minx := x[0]
	for i := range x {
		if x[i] < minx {
			minx = x[i]
		}
	}
	fmt.Println("Minimum number in array is", minx)
}
