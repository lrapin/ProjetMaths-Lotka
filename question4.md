# Question 4

Grâce au théorème de Cauchy-Lipschitz, nous avons qu'il existe une unique solution mamximale locale (défini sur un intervalle de temps fini) pour toutes conditions initiales dans $\mathbb{R_{>0}^2}$. Nous cherchons maintenant à prolonger ces solutions dans $\mathbb{R}$ tout entier.

Nous commencons par calculer la dérivée de $H(x1, x2) = δx1 − γ ln(x1) + βx2 − α ln(x2)$ :

$\frac{d}{dt}(H(x_1, x_2)) = < \nabla H(x_1, x_2), f(x_1, x_2)>$

Donc
$\begin{matrix}
    &   \begin{pmatrix}
        \alpha x_1 - \beta  x_1 x_2\\
        -\gamma x_2 + \delta x_1 x_2
        \end{pmatrix}   \\
\frac{d}{dt}(H(x_1, x_2)) =
\begin{pmatrix}
\delta - \frac{\gamma}{x_1} & \beta - \frac{\alpha}{x_2}\\
\end{pmatrix}
    &   \begin{pmatrix}
        \;\;\;0\;\;\;\\
        \end{pmatrix}
\end{matrix}$

Ainsi $H$ est une constante : $H(x_1, x_2) = H_0$. Nous pouvons ainsi montrer que $f(x_1, x_2)$ est bornée.

En effet, $\exists A, B> 0,\; \forall x_1>A, \forall x_2>B,$
$
\left\{\begin{matrix}
\gamma*ln(x_1) < \frac{\delta x_1}{2}\\
\alpha*ln(x_2) < \frac{\beta x_2}{2}
\end{matrix}\right.
$

Ainsi, si $(x_1, x_2)\notin[-A, A]\times[-B, B]$, $ H_0 > \frac{1}{2}*(\delta x_1 +\beta x_2)$

donc $(x_1(t), x_2(t))$ est bornée. En appliquant la réciproque du théorème du domaine maximal d'existence, on prouve alors que toute solution maximale est définie sur $\mathbb{R}$ tout entier.
