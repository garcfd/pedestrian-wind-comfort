

      program pearson_corr

      implicit none

      integer, parameter :: nmax = 80
      real,allocatable   :: x(:), y(:)
      real               :: mean_x, mean_y, cov, var_x, var_y, r
      integer            :: i, dum
      real               :: a, b

      allocate(x(nmax), y(nmax))

C     Open files
      open(10, file='exptwest.dat', status='old')
      open(11, file='unsprobe.dat', status='old')

      read(10,*)
      read(10,*)

      do i = 1,nmax
        read(10,*) dum,x(i)
        read(11,*) dum,y(i)
      end do

      close(10); close(11)

C     Compute means
      mean_x = sum(x)/nmax
      mean_y = sum(y)/nmax

C     Compute covariance and variances
      cov   = sum( (x - mean_x)*(y - mean_y) ) / nmax
      var_x = sum( (x - mean_x)**2 ) / nmax
      var_y = sum( (y - mean_y)**2 ) / nmax

C     Pearson correlation coefficient
      if (var_x*var_y > 0.0) then
        r = cov / sqrt(var_x*var_y)
      else
        r = 0.0
      end if

      print '(A,F12.8)', ' Pearson r = ', r

      end


