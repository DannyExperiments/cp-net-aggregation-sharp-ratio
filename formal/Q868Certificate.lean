import Std

namespace ParentRestricted

def vote (n context omitted : Nat) : Bool :=
  (List.range n).any fun i => i != omitted && context.testBit i

def ones (n context : Nat) : Nat :=
  (List.range n).countP fun i => vote n context i

def freeCost (n : Nat) : Nat :=
  ((List.range (2 ^ n)).map fun x => min (ones n x) (n - ones n x)).sum

def pairedOnes (n x omitted : Nat) : Nat :=
  ones n x + ones n (x + 2 ^ omitted)

def restrictedCost (n omitted : Nat) : Nat :=
  (((List.range (2 ^ n)).filter fun x => !(x.testBit omitted)).map fun x =>
    min (pairedOnes n x omitted) (2 * n - pairedOnes n x omitted)).sum

theorem unrestricted_four : freeCost 4 = 4 := by decide +kernel

theorem every_restricted_four :
    (List.range 4).all (fun i => restrictedCost 4 i == 6) = true := by
  decide +kernel

theorem zero_fiber_four :
    (List.range 4).all (fun i => pairedOnes 4 0 i == 3 &&
      (8 - pairedOnes 4 0 i) == 5) = true := by
  decide +kernel

theorem violation_four :
    (List.range 4).all (fun i => 4 * freeCost 4 < 3 * restrictedCost 4 i) = true := by
  decide +kernel

theorem pair_bound (t k : Nat) (h : 1 ≤ k) :
    2 * k * (t - k) ≤ 2 * k * (t - 1) := by
  exact Nat.mul_le_mul_left (2 * k) (Nat.sub_le_sub_left h t)

#print axioms unrestricted_four
#print axioms every_restricted_four
#print axioms zero_fiber_four
#print axioms violation_four
#print axioms pair_bound

end ParentRestricted
