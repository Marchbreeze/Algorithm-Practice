/*
<1922. 네트워크 연결>
골드4
https://www.acmicpc.net/problem/1922
*/

import java.io.*
import java.util.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val m = readLine().toInt()

    // 간선 정보
    data class Edge(val u: Int, val v: Int, val cost: Int)
    val edges = mutableListOf<Edge>()
    repeat(m) {
        val (a, b, c) = readLine().split(" ").map{ it.toInt() }
        edges.add(Edge(a, b, c))
    }

    // 비용 오름차순 정렬
    edges.sortBy { it.cost }

    // 부모 테이블
    val parent = IntArray(n + 1) { it }

    fun findParent(x: Int): Int {
        if (parent[x] == x) {
            return x
        } else {
            parent[x] = findParent(parent[x])
            return parent[x]
        }
    }

    fun unionParent(a: Int, b: Int) {
        val rootA = findParent(a)
        val rootB = findParent(b)
        if (rootA < rootB) {
            parent[rootB] = rootA
        } else {
            parent[rootA] = rootB
        }
    }

    var totalCost = 0
    for ((u, v, cost) in edges) {
        if (findParent(u) != findParent(v)) {
            unionParent(u, v)
            totalCost += cost
        }
    }

    println(totalCost)
}