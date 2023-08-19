export function Logo(props: React.ComponentPropsWithoutRef<'svg'>) {
  return (
    <svg width="500" height="100" viewBox="0 0 500 100" {...props}>
      {/* Text */}
      <text x="20" y="70" font-family="Arial" font-size="50" font-weight="bold" fill="#2D3748">
        Django Realms
      </text>
      {/* Inner circles representing multiple realms or tenants with different colors */}
      <circle cx="410" cy="35" r="10" fill="#2D3748"/> {/* Slate color */}

      <circle cx="440" cy="35" r="10" fill="#2D3748"/> {/* Slate color */}
      <circle cx="410" cy="65" r="10" fill="#4ade80"/> {/* Green color */}
      <circle cx="440" cy="65" r="10" fill="#2D3748"/> {/* Slate color */}
    </svg>
  )
}
