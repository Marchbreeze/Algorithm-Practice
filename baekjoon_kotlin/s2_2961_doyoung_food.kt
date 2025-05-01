/*
<2961. 도영이가 만든 맛있는 음식>
실버2
https://www.acmicpc.net/problem/15649
*/

import java.io.*
import java.util.*
import java.util.ArrayDeque
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val foods = mutableListOf<Pair<Int, Int>>()
    repeat(n) {
        val (s, b) = readLine().split(" ").map { it.toInt() }
        foods.add(Pair(s, b))
    }

    var answer = Int.MAX_VALUE
    // 인덱스, 총 신맛, 총 쓴맛, 개수
    val q = LinkedList<IntArray>()
    q.offer(intArrayOf(0,1,0,0))

    while (q.isNotEmpty()) {
        val (idx, sour, bitter, count) = q.poll()
        if (idx == n) {
            if (count != 0) answer = minOf(answer, abs(sour - bitter))
            continue
        }
        val (foodSour, foodBitter) = foods[idx]
        q.offer(intArrayOf(idx+1, sour, bitter, count))
        q.offer(intArrayOf(idx+1, sour * foodSour, bitter + foodBitter, count+1))
    }
    println(answer)
}