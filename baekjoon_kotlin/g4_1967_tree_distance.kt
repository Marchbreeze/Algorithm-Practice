/*
<1967. 트리의 지름>
골드4
https://www.acmicpc.net/problem/1967
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val graph = Array(n+1) { mutableListOf<Pair<Int, Int>>() }
    repeat(n-1) {
        val (a, b, c) = readLine().split(" ").map{ it.toInt() }
        graph[a].add(b to c)
        graph[b].add(a to c)
    }

    val visited = BooleanArray(n+1) { false }
    var maxCost = 0
    var count = 0

    fun dfs(node: Int) {
        var hasNext = false
        for ((next, cost) in graph[node]) {
            if (!visited[next]) {
                hasNext = true
                visited[next] = true
                count += cost
                dfs(next)
                count -= cost
                visited[next] = false
            }
        }
        if (!hasNext) maxCost = maxOf(maxCost, count)
    }

    for (i in 1..n) {
        visited[i] = true
        dfs(i)
        visited[i] = false
    }
    println(maxCost)
}