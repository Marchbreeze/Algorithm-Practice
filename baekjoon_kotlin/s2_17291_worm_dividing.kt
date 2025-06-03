/*
<17291. 새끼치기>
실버2
https://www.acmicpc.net/problem/17291
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val dp = IntArray(21)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7
    for (i in 5..20) {
        if (i%2 == 0) {
            dp[i] = dp[i-1]*2 - dp[i-4] - dp[i-5]
        } else {
            dp[i] = dp[i-1]*2
        }
    }
    println(dp[n])
}