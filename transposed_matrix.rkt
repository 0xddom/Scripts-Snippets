;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; This scheme functions take a matrix
; on the form '((1 4 7) (2 5 8) (3 6 9))
; and returns it on the form
; '(1 2 3 4 5 6 7 8 9)
; 
; (c) Daniel Domínguez, 2015
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

#lang racket

(define m Your matrix here)

(define (g listas)
 (if (empty? listas)
 '()
 (append (list (caar listas)) (g (cdr listas)))))

(define (h listas)
 (if (empty? listas)
 '()
 (append (list (cdar listas)) (h (cdr listas)))))

(define (i lista)
 (if (empty? (cdr lista))
 (empty? (car lista))
 (and (empty? (car lista)) (i (cdr lista)))))

(define (f lista)
 (if (i lista)
 '()
 (append (g lista) (f (h lista)))))
 
(f m)
