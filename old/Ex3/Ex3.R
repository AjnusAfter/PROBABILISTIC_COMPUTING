# a
a = 3973
c = 0
M = 2^31 - 1
n_samples = 10000


LCG <- function(seed, a, c, M, n_samples)
{
  x = seed
  u = NULL
  
  for (i in 1:n_samples)
  {
    nx = (a * x + c) %%  M
    u = c(u, as.double(nx) / as.double(M))
    x = nx
  }
  
  return (u)
}


CARA_OU_COROA <- function(U, p)
{
  n = length(U)
  CC = NULL
  
  for (i in 1:n)
  {
    if (U[i] < (1.0 - p))
    {
      CC = c(CC, 0)   #cara
    }
    else
    {
      CC = c(CC, 1)     #coroa
    }
  }
  
  return (CC)
}

U = LCG(3, a, c, M, n_samples)
hist(U, col = "purple")
CC = CARA_OU_COROA(U, 0.5)
print(sum(CC))