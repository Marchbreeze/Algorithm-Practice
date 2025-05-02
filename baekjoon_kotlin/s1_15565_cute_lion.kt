/*
<15565. 귀여운 라이언>
실버1
https://www.acmicpc.net/problem/15565
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(" ").map{ it.toInt() }
    val arr = readLine().split(" ").map{ it.toInt() }.toIntArray()

    var left = 0
    var right = 0
    var answer = Int.MAX_VALUE
    var count = 0

    // 1(라이언 인형)이면 1, 아니면 0 반환
    fun isLion(item: Int): Int {
        return if (item == 1) 1 else 0
    }

    // K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기
    while (true) {
        when {
            count >= k -> {
                answer = minOf(answer, right-left)
                count -= isLion(arr[left])
                left += 1
            }

            right == n -> break
            
            else -> {
                count += isLion(arr[right])
                right += 1
            }
        }
    }
    if (answer == Int.MAX_VALUE) println(-1) else println(answer)
}