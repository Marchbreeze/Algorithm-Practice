/*
<1991. 트리 순회>
실버1
https://www.acmicpc.net/problem/1991
*/

import java.io.*
import java.util.*
import kotlin.math.*

private val nodes = mutableMapOf<Char, Pair<Char, Char>>()

private fun preOrder(node: Char) {
    if (node == '.') return
    val (left, right) = nodes[node]!!
    print(node)
    preOrder(left)
    preOrder(right)
} 

private fun inOrder(node : Char) {
    if (node == '.') return
    val (left, right) = nodes[node]!!
    inOrder(left)
    print(node)
    inOrder(right)
} 

private fun postOrder(node : Char) {
    if (node == '.') return
    val (left, right) = nodes[node]!!
    postOrder(left)
    postOrder(right)
    print(node)
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    repeat(n) {
        val (node, left, right) = readLine().split(" ")
        nodes[node[0]] = left[0] to right[0]
    }

    preOrder('A')
    print("\n")
    inOrder('A')
    print("\n")
    postOrder('A')
    print("\n")
}