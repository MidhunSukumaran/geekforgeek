

def check_all_one(ar, k):
    i = 0
    n = len(ar)
    first_zero = None
    last_one = None
    last_zero_validated = True
    while i < n:
        if ar[i] == 1:
            last_one = i
            if first_zero is not None and (i - first_zero) > k:
                return "No"
            else:
                last_zero_validated = True

        else:
            if last_zero_validated:
                first_zero = i

            if ((last_one is not None) and (i - last_one) > k) or last_one is None:
                if i == n - 1:
                    return "No"
                else:
                    last_zero_validated = False
            else:
                last_zero_validated = True

        i += 1

    return "Yes"


ar = list(map(int, input().split(", ")))
k = int(input())
print(check_all_one(ar, k))
