/*
<2293. 동전 1>
골드4
https://www.acmicpc.net/problem/2293
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(" ").map{ it.toInt() }
    val coins = IntArray(n) { readLine().toInt() }
    // i번쨰 : i-1 + i-2 + i-5
    // dp 테이블 설정
    val dp = IntArray(k+1) {0}
    dp[0] = 1

    // 코인을 하나씩 추가하며, 만들수있는 개수 추가해나가기
    coins.forEach { coin ->
        for (i in coin..k) {
            dp[i] += dp[i-coin]
        }
    }
    println(dp[k])
}