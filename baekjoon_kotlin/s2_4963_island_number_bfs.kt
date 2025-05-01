/*
<4963. 섬의 개수>
실버2
https://www.acmicpc.net/problem/4963
*/

import java.io.*
import java.util.*

// 가로, 세로, 대각선 8방향
private val dy = intArrayOf(-1,  0,  1,  0, 1, 1, -1, -1)
private val dx = intArrayOf( 0, -1,  0,  1, 1, -1, 1, -1)

// 격자 내 위치 여부
private fun isOutOfRange(y: Int, x: Int, w: Int, h: Int): Boolean = y < 0 || x < 0 || y >= h || x >= w

// 공통 리스트
private lateinit var map : Array<IntArray>

// 접근 가능 시 모든 땅 밟고 true 반환
private fun bfs(startY: Int, startX: Int, w: Int, h: Int) {
    // 큐에 Pair(y,x) 를 담아 사용
    val q = LinkedList<Pair<Int,Int>>()
    q.offer(startY to startX)

    // 반복문 진행
    while (q.isNotEmpty()) {
        val (y, x) = q.poll()
        for (d in 0..7) {
            // 다음 방향 진행
            val ny = y + dy[d]
            val nx = x + dx[d]

            // 진행 가능 여부 확인
            if (isOutOfRange(ny, nx, w, h) || map[ny][nx] != 1) continue

            // 가능한 경우 큐에 추가
            q.offer(ny to nx)
            map[ny][nx] = 0
        }
    }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    while (true) {
        val (w, h) = readLine().split(" ").map { it.toInt() }
        if (w == 0 && h == 0) break
        map = Array(h) { readLine().split(" ").map { it.toInt() }.toIntArray() }
        var count = 0
        for (y in 0 until h) {
            for (x in 0 until w) {
                if (map[y][x] == 1) {
                    count += 1
                    bfs(y, x, w, h)
                }
            }
        }
        println(count)
    }
}