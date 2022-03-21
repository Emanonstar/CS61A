(define (split-at lst n)
  (if (null? lst) (cons (list) nil)
	(if (= n 0) 
		(cons (list) lst)
		(cons (cons (car lst) (car (split-at (cdr lst) (- n 1))))
			(cdr (split-at (cdr lst) (- n 1)))
		)
    )
  )
)



(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons (eq? (eval expr) (car case)) (cdr case)))
    			cases))
)
