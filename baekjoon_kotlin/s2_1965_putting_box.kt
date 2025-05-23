/*
<1965. 상자넣기>
실버2
https://www.acmicpc.net/problem/1965
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val boxs = readLine().split(" ").map{ it.toInt() }

    val dp = IntArray(n) {1}
    for (i in 0 until n) {
        for (j in 0 until i) {
            if (boxs[i] > boxs[j]) {
                dp[i] = maxOf(dp[i], dp[j] + 1)
            }
        }
    }
    println(dp.max())
}