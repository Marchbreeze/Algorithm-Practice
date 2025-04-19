/*
<2178. 미로 탐색>
실버1
https://www.acmicpc.net/problem/2178
*/

import java.io.*
import java.util.*
import kotlin.collections.ArrayDeque

val dx = intArrayOf(1,-1,0,0)
val dy = intArrayOf(0,0,1,-1)

fun isOutOfRange(y: Int, x: Int, n: Int, m:Int): Boolean = y < 0 || x < 0 || y >= n || x >= m

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    // 입력
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val maze = Array(n) { readLine().map { it - '0' }.toIntArray() }
    
    // 미로 시작
    val q = LinkedList<Pair<Int, Int>>()
    q.offer(0 to 0)

    // BFS 진헹
    while (q.isNotEmpty()) {
        val (y, x) = q.poll()
        for (i in 0..3) {
            val ny = y + dy[i]
            val nx = x + dx[i]
            if (isOutOfRange(ny, nx, n, m)) continue
            if (maze[ny][nx] == 1) {
                q.offer(ny to nx)
                maze[ny][nx] = maze[y][x] + 1
            }
        }
    }

    // 출력
    println(maze[n-1][m-1])
}