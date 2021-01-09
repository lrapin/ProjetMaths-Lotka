# Question 1

## **Dynamique du système**

On suppose que les proies se reproduisent de manière exponentielle et que la diminution de leur population est liée aux recontres avec les prédateurs.
On suppose également que les prédateurs ont une mortalité exponentielle. La population des prédateurs augmente lorsqu'ils rencontrent des proies.

|$\dot{x_1} =$|$\alpha x_1$|$-\beta x_1 x_2$|
|:--------------:|:------------------:|:---------------------------:|
|évolution proies| naissance naturelle proies|rencontre proies prédateurs|
</br>

|$\dot{x_2} =$|$-\gamma x_2$|$+\delta x_1 x_2$|
|:------------------:|:-------------------------------:|:-----------:|
|évolution prédateurs|mortalité naturelle prédateurs|rencontre proie prédateurs|
</br>

## **Points d'équilibre**

$x$ est un point d'équilibre si et seulement $\dot{x} = 0$

$\Leftrightarrow
\begin{pmatrix}
x_1 = 0 & ou & \alpha = \beta x_2 \\
x_2 = 0 & ou & \gamma = \delta x_1
\end{pmatrix}$

$\Leftrightarrow
x = 0 \;$ ou $\; \bar{x} = (\frac{\gamma}{\delta}, \frac{\alpha}{\beta})$

En effet, si $x_1 = 0\,$, alors $x_2 = 0$ nécessairement car il n'est pas possible que $x_1 = \frac{\gamma}{\delta} > 0$
