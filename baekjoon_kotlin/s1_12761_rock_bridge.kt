/*
<12761. 돌다리>
실버1
https://www.acmicpc.net/problem/12761
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (a, b, n, m) = readLine().split(" ").map{ it.toInt() }

    // Pair : 현위치, 횟수
    val q = LinkedList<Pair<Int,Int>>()
    val visited = BooleanArray(100001) { false }

    q.offer(n to 0)
    visited[n] = true
    while (q.isNotEmpty()) {
        val (current, count) = q.poll()
        if (current == m) {
            println(count)
            break
        }
        val moves = listOf(
            current + 1,
            current - 1,
            current + a,
            current - a,
            current + b,
            current - b,
            current * a,
            current * b
        )
        for (next in moves) {
            if (next in 0..100000 && !visited[next]) {
                visited[next] = true
                q.offer(next to (count + 1))
            }
        }
    }
}