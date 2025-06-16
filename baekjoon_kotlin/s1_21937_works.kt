/*
<21937. 작업>
실버1
https://www.acmicpc.net/problem/21937
*/

import java.io.*
import java.util.*
import kotlin.math.*

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m) = readLine().split(" ").map{ it.toInt() }
    val works = Array(n+1) { mutableListOf<Int>() }
    repeat(m) {
        val (a, b) = readLine().split(" ").map{ it.toInt() }
        works[b].add(a)
    } 
    val x = readLine().toInt()

    val visited = BooleanArray(n+1) {false}
    visited[x] = true

    val stack = mutableListOf<Int>()
    stack.add(x)

    var count = 0
    while (stack.isNotEmpty()) {
        val work = stack.removeLast()
        works[work].forEach { item ->
            if (!visited[item]) {
                visited[item] = true
                stack.add(item)
                count += 1
            }
        }
    }
    println(count)
}