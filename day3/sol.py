import jax.numpy as jnp
from jax import jit


@jit
def gamma_calc(data: jnp.ndarray) -> tuple[float, float]:
    added = jnp.sum(data, axis=0)
    cutoff = data.shape[1] // 2
    print(cutoff)
    return jnp.where(added > cutoff, 1, 0)


def main():
    with open("input") as f:
        data = jnp.asarray([[int(y) for y in x.strip()] for x in f.readlines()])
    print(data)
    print(gamma_calc(data))


if __name__ == "__main__":
    main()
