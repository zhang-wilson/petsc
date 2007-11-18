#!/bin/env python

configure_options = [
  '--with-f90-interface=solaris',
  '--with-mpi-dir=/home/petsc/soft/solaris-9-lam/lam-6.5.8',
  '--with-mpiexec=/sandbox/petsc/petsc-dev/bin/mpiexec.lam'
  ]

if __name__ == '__main__':
  import configure
  configure.petsc_configure(configure_options)
