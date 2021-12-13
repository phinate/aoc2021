import jax.numpy as jnp
from jax import jit


@jit
def gamma_calc(data: jnp.ndarray) -> tuple[jnp.ndarray, jnp.ndarray]:
    added = jnp.sum(data, axis=0)
    cutoff = data.shape[0] // 2
    return jnp.where(added > cutoff, 1, 0), jnp.where(added > cutoff, 0, 1)


def main():
    with open("input") as f:
        data = jnp.asarray([[int(y) for y in x.strip()] for x in f.readlines()])
    g, e = gamma_calc(data)
    gamma = int("".join([str(x) for x in g]), 2)
    epsilon = int("".join([str(x) for x in e]), 2)
    print(gamma * epsilon)


if __name__ == "__main__":
    main()
