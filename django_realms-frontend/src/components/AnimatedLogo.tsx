// import django_realms-frontend/src/styles/AnimatedLogo.module.css
import React from 'react'
import styles from '@/styles/AnimatedLogo.module.css'


export function AnimatedLogo(props: React.ComponentPropsWithoutRef<'svg'>) {
  return (
    <svg id="a" width="1000" height="1000" viewBox="0 0 1000 1000" {...props}>
      {/* Inner circles representing multiple realms or tenants with different colors */}
      <circle className={`${styles.flicker} ${styles.topleft}`} cx="52.99" cy="52.99" r="49.49" fill="#2D3748" />
      <circle className={`${styles.flicker} ${styles.bottomleft}`} cx="52.99" cy="225.17" r="49.49" fill="#4ade80" />
      <circle className={`${styles.flicker} ${styles.topright}`} cx="225.01" cy="52.99" r="49.49" fill="#2D3748" />
      <circle className={`${styles.flicker} ${styles.bottomright}`} cx="225.01" cy="225.17" r="49.49" fill="#2D3748" />
      <circle className={`${styles.flicker} ${styles.center}`} cx="137.97" cy="139.84" r="49.49" fill="#4ade80" />
    </svg>
  )
}