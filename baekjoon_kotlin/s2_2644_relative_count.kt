/* 
<2644. 촌수계산>
실버2
https://www.acmicpc.net/problem/2644
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    // 입력
    val n = readLine().toInt()
    val (start, target) = readLine().split(" ").map { it.toInt() }
    val m = readLine().toInt()

    // 1) 인접 리스트로 그래프 구성 (양방향)
    val graph = Array(n + 1) { mutableListOf<Int>() }
    repeat(m) {
        val (u, v) = readLine().split(" ").map { it.toInt() }
        graph[u].add(v)
        graph[v].add(u)
    }

    // 방문 체크
    val visited = BooleanArray(n + 1) { false }
    visited[start] = true

    // DFS 구현
    val stack = mutableListOf(start to 0)  // Pair(node, depth)
    var result = -1

    while (stack.isNotEmpty()) {
        val (current, depth) = stack.removeAt(stack.lastIndex)
        if (current == target) {
            result = depth
            break
        }
        for (next in graph[current]) {
            if (!visited[next]) {
                visited[next] = true
                stack.add(next to depth + 1)
            }
        }
    }

    // 5) 실행 & 출력
    println(result)
}