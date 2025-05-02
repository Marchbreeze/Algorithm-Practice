/*
<2343. 기타 레슨>
실버1
https://www.acmicpc.net/problem/2343
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val arr = readLine().split(" ").map { it.toInt() }.toIntArray()

    // 파라매트릭 서치 - 가능한 최소 디스크 크기 찾기
    var start = arr.maxOrNull() ?: 0
    var end = arr.sum()
    var answer = 0
    while (start <= end) {
        val mid = (start + end) / 2
        var count = 0
        var eachCount = 0
        arr.forEach { item ->
            if (eachCount + item > mid) {
                count += 1
                eachCount = 0
            }
            eachCount += item
        }
        if (count < m) {
            answer = mid
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    println(answer)
}