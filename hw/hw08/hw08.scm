(define (rle s)
  (define (helper num cnt s)
    (if (null? s)
        (cons-stream (list num cnt) nil)
        (if (= num (car s))
            (helper num (+ cnt 1) (cdr-stream s))
            (cons-stream (list num cnt) (helper (car s) 1 (cdr-stream s)))
        )
    )
  )
  (if (null? s) nil
      (helper (car s) 1 (cdr-stream s))
  ) 
)



(define (group-by-nondecreasing s)
    (define (helper ele num s)
        (if (null? s)
            (cons-stream ele nil)
            (if (< (car s) num)
                (cons-stream ele (helper (list (car s)) (car s) (cdr-stream s)))
                (helper (append ele (list (car s))) (car s) (cdr-stream s))
            )
        )
    )
    (if (null? s) nil
      (helper (list (car s)) (car s) (cdr-stream s))
    )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

