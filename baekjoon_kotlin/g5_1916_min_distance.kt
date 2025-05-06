/*
<1916. 최소비용 구하기>
골드5
https://www.acmicpc.net/problem/1916
*/

import java.io.*
import java.util.*
import java.util.PriorityQueue

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val m = readLine().toInt()
    val graph = Array(n+1) { mutableListOf<Pair<Int, Int>>() } 
    repeat(m) {
        val (a, b, c) = readLine().split(" ").map{ it.toInt() }
        graph[a].add(b to c)
    }
    val (start, end) = readLine().split(" ").map { it.toInt() }

    val distance = IntArray(n + 1) { Int.MAX_VALUE }
    distance[start] = 0

    val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.first })
    pq.offer(0 to start)

    while (pq.isNotEmpty()) {
        val (dist, now) = pq.poll()
        if (distance[now] < dist) continue

        for ((next, weight) in graph[now]) {
            val cost = dist + weight
            if (cost < distance[next]) {
                distance[next] = cost
                pq.offer(cost to next)
            }
        }
    }

    println(distance[end])
}