// 14. 最长公共前缀.go
package main

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	res := strs[0]
	size := len(strs)
	for i := 1; i < size; i++ {
		j := 0
		for ; j < len(strs[i]) && j < len(res); j++ {
			if res[j] != strs[i][j] {
				break
			}
		}

		res = res[:j]
	}
	return res
}
