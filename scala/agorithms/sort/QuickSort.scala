class QuickSort {
  def sort(k: Array[Int]) : Array[Int] = {
    if (k.length < 2) k
    else {
      else {
        val pivot = k(k.length / 2)
        sort (k filter (pivot >)) ++ (k filter (pivot == )) ++ sort (k filter(pivot <))
      }
    }
  }
}
