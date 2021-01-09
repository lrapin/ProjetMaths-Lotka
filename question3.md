# Question 3

Les équations de Lotka-Volterra peuvent se réécrire : $\dot{x} = f(x)$

avec
$f :
\begin{matrix}
\mathbb{R}_{>0}\times \mathbb{R}_{>0} \rightarrow \mathbb{R}\times \mathbb{R} \\
\;\;\;\;\;(x_1, x_2) \rightarrow
\begin{pmatrix}
\alpha x_1 - \beta  x_1 x_2\\
-\gamma x_2 + \delta x_1 x_2
\end{pmatrix}
\end{matrix}
$
est continue

et comme

$(t,x) \rightarrow \partial_xf(t, x) =
\begin{pmatrix}
 \alpha - \beta x_2 & -\beta x_1 \\
 \delta x_2 & -\gamma + \delta x_1
\end{pmatrix}$ existe et est continue sur $\mathbb{R} \times \mathbb{R_{>0}^2}$ alors f est continuement différentiable par rapport à $x$.

Par le théorème de Cauchy-Lipschitz, pour tout $x_0 \in \mathbb{R_{>0}^2}$, il existe une solution maximale unique $x : I \rightarrow \mathbb{R^2}$ dans $S_f(x_0)$

Si $x_1(t_0) = 0$ et $x_2(t_0) > 0$, alors par le théorème de Cauchy-Lipschitz,

$
\left\{\begin{matrix}
x_1(t) = x_1(t_0) = 0 \;\;\;\;\;\;\;\;\;\\
x_2(t) = x_2(t_0) * e^{-\gamma(t-t_0)}
\end{matrix}\right.
\;\;$
est l'unique solution passant par $(0, x_2(t_0))$.

De même, si $x_1(t_0) > 0$ et $x_2(t_0) = 0$,

$
\left\{\begin{matrix}
x_1(t) = x_1(t_0) * e^{\alpha(t-t_0)}\\
x_2(t) = x_2(t_0) = 0 \;\;\;\;\;\;\;\;\;
\end{matrix}\right.
\;\;$
est l'unique solution passant par $(x_1(t_0), 0)$.

Ainsi, si
$
\left\{\begin{matrix}
x_1(t_0) > 0\\
x_2(t_0) > 0
\end{matrix}\right.
\;\;$
alors
$
\left\{\begin{matrix}
x_1(t) > 0\\
x_2(t) > 0
\end{matrix}\right.
\;\forall t\;$

En effet, si $\exists \tau, \;x_1(\tau) = 0$, alors $\forall t,\, x_1(t) = 0$, notamment pour $t=t_0$, ce qui est absurde car $x_1(t_0) > 0$. De même par rapport à $x_2$. De plus, il ne peut pas exister de $t$ tel que $x_1(t) <0$ car on se retrouverait dans le cas précédent par théorème des valeurs intermédiaires.
