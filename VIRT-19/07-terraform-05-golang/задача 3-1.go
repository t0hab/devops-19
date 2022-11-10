package main

import "fmt"

func main() {
	fmt.Print("Enter meters: ")
	var input_meters float64
	fmt.Scanf("%f", &input_meters)

	output_feets := input_meters * 0.3048

	fmt.Println(input_meters, "meters euqals", output_feets, "feet")
}
