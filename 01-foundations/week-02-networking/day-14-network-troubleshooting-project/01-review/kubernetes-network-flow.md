# Kubernetes Network Flow

Focus on:

```
Ingress
   ↓
Service
   ↓
EndpointSlice
   ↓
Pod
   ↓
Container
```

And:

```
Service selector
       ↓
Pod labels
       ↓
Endpoints
```