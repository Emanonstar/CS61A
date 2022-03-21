(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
      ((> num 0) 1)
      ((< num 0) -1)
      (else 0))
)


(define (square x) (* x x))

(define (pow x y)
  (if (= x 0) (if (= y 0) "Not defined" 0)
      (if (= y 0) 1
          (if (even? y) (square (pow x (quotient y 2)))
              (* x (square (pow x (quotient y 2))))
            )
        )
    )
)


(define (unique s)
  (if (null? s) nil
      (cons (car s)
            (unique (filter (lambda (e) (not (equal? e (car s)))) (cdr s)))
        )
    )
)


(define (replicate x n)
  (define (replicate_tail x n lst)
      (if (= n 0) lst
          (replicate_tail x (- n 1) (cons x lst))
        )
    )
    (replicate_tail x n nil)
  )


(define (accumulate combiner start n term)
  (if (= n 0) start
       (accumulate combiner (combiner start (term n)) (- n 1) term)
  )
)


(define (accumulate-tail combiner start n term)
  (if (= n 0) start
       (accumulate-tail combiner (combiner start (term n)) (- n 1) term)
  )
)


(define-macro (list-of map-expr for var in . lst)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,(if (null? (cdr lst)) #t (caddr lst))) ,(car lst)))
  ;(list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) (if (null? (cdr lst)) #t (caddr lst))) (car lst)))
)

