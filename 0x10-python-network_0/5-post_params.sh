#!/bin/bash
# Script that sends a POST request to the passed URL, and displays the body of the response.
curl -s "$1" -X POST -d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD"
