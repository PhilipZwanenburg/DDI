;; Local variables specific to this project.
;;
;; The add-hook functionality requires that the following code is included in the main dotfile:
;; ;; Provide a new MAJORMODE-local-vars-hook
;; ;; reference: https://emacs.stackexchange.com/a/29662
;; (add-hook 'hack-local-variables-hook 'run-local-vars-mode-hook)
;; (defun run-local-vars-mode-hook ()
;;   "Run a hook for the major-mode after the local variables have been processed."
;;   (run-hooks (intern (concat (symbol-name major-mode) "-local-vars-hook"))))
;;
;; usage:
;; ((nil . ((eval . (add-hook 'c++-mode-local-vars-hook  (lambda () (c-set-offset 'innamespace '+))))
;;          )
;;       )
;;  )
;;
;; Reference:
;; https://www.gnu.org/software/emacs/manual/html_node/emacs/Directory-Variables.html

((nil . ((fill-column . 100)
         (eval . (add-hook 'python-mode-local-vars-hook  (lambda () (modify-syntax-entry ?_ "w")))) ; Make _ symbols count as part of words.
         )
      )
 (c-mode (helm-make-build-dir . ""))
 )
