echo -e "Installig python3... \c"
sudo apt -y install python3 \
                    python3-pip \
                    python3-venv \
                    idle3  > /dev/null
echo -e "[OK]\n"

echo -e "Creating virtual environment... \c"
python3 -m venv venv
source venv/bin/activate
echo "[Activated] \n"

echo -e "Preparing... "
pip install --upgrade pip
pip install -r req.txt
