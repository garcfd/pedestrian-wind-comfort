
      program main

      implicit none

      integer ,parameter :: imax=80,jmin=50,jmax=100

      integer :: i,j
      real    :: dummy,speed(imax,jmax),avespeed


      character(len=30) :: filename

C-----read csv files
      do j = 1, jmax

        write(filename, '(A,I2.2,A)') '../csv-files/test_',j-1,'.csv'
        open(10, file=trim(filename), status='unknown')
        write(6,*) "Reading file", trim(filename)
        read(10,*)

        do i = 1,imax
          read(10,*)dummy,dummy,dummy,speed(i,j)
CCC       write(6,*)i,j,speed(i,j)
        enddo
        close(10)

      end do

C-----write mean data

      open(10, file="unsprobe.dat", status='unknown')
      do i = 1, imax

        avespeed = 0.0
        do j = jmin, jmax
          avespeed = avespeed + speed(i,j)
        end do
        avespeed = avespeed/real(jmax-jmin+1)

        write(10,*)i,avespeed
        write(6,*) i,avespeed

      end do
      close(10)

      end









