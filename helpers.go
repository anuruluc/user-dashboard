
import "sync"
var (
    mutex sync.Mutex
    counter int
)
func Increment() int {
    mutex.Lock()
    defer mutex.Unlock()
    counter++
    return counter
}


func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

