/*
<5567. 결혼식>
실버2
https://www.acmicpc.net/problem/5567
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val m = readLine().toInt()
    //  인접 리스트 입력
    val adj = MutableList(n + 1) { mutableListOf<Int>() }
    repeat(m) {
        val (from, to) = readLine().split(" ").map { it.toInt() }
        adj[from].add(to)
        adj[to].add(from)
    }

    // 연결된 사람 수 찾기 (시작 1)
    var count = 0
    val visited = BooleanArray(n+1) {false}
    val q = LinkedList<Pair<Int, Int>>()

    visited[1] = true
    q.offer(Pair(1,0))

    while (q.isNotEmpty()) {
        val (idx, depth) = q.poll()

        adj[idx].forEach { next ->
            if (!visited[next]) {
                visited[next] = true
                count += 1
                if (depth < 1) q.offer(Pair(next, depth + 1))
            }
        }
    }
    println(count)
}