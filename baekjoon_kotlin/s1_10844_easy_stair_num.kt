/*
<10844. 쉬운 계단수>
실버1
https://www.acmicpc.net/problem/10844
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val dp = Array(n+1) { IntArray(10) {0} }
    for (n in 1..9) dp[1][n] = 1

    val mod = 1000000000
    for (i in 2..n) {
        for (j in 0..9) {
            // 값이 1e9보다 커지면 Int 범위를 넘고, 오버플로우된 음수 값들이 담김
            dp[i][j] = when (j) {
                0    -> dp[i-1][1]
                9    -> dp[i-1][8]
                else -> dp[i-1][j-1] + dp[i-1][j+1]
            } % mod
        }
    }
    var answer = 0
    dp[n].forEach { value ->
        answer = (answer + value) % mod
    }
    println(answer % mod)
}