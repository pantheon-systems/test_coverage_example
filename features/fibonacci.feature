Feature: Fibonacci sequence
	As a math fanatic
	I want to be able to generate fibonacci sequences
	So that I can have endless fun on my computer

	Scenario Outline: compute the fibonacci sequence for N integers
		Given a count of "<count>"
		When I call the fibonacci function
		Then it should return a sequence "<sequence>"
		And the sequence should be a sequence of integers

		Examples: counts
			| count | sequence		 |
			| 1		| 1				 |
			| 3		| 1,1,2			 |
			| 5		| 1,1,2,3,5		 |
			| 7		| 1,1,2,3,5,8,13 |

	Scenario: return nothing for a negative count
		Given a count of "-1"
		When I call the fibonacci function
		Then it should return an empty sequence

	Scenario: fail for non-integer count
		Given a non-integer count of "pantheon"
		When I call the fibonacci function
		Then it should throw a TypeError exception