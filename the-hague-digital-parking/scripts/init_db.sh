#!/bin/bash

echo "📦 Initializing mock database..."
touch parking_data.db
echo '{"initialized": true}' > parking_data.db
echo "✅ DB ready."

