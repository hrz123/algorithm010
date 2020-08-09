// 1014. 最佳观光组合.go
package __15_6_21每日一题

func maxScoreSightseeingPair(A []int) int {
	res := 0
	mx := A[0]
	for i := 1; i < len(A); i++ {
		tmp1 := mx + A[i] - i
		if res < tmp1 {
			res = tmp1
		}
		tmp2 := A[i] + i
		if mx < tmp2 {
			mx = tmp2
		}
	}
	return res
}
