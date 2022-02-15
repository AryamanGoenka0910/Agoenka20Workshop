(define fact
    (lambda (n)
        (if (= n 1)
        1
        (* (fact(- n 1)) n)
        )
    )
)

(define fib
    (lambda (n)
        (if (<= n 1)
        n
        (+ (fib(- n 2)) (fib(- n 1)))
        )
    )
)